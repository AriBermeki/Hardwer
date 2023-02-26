import pyvisa

class InstrumentController:
    def __init__(self, visa_resource_manager):
        self.visa_resource_manager = visa_resource_manager
        self.instruments = {}
        self.functions = []

    def add_instrument(self, instrument_name, visa_resource_string):
        instrument = self.visa_resource_manager.open_resource(visa_resource_string)
        self.instruments[instrument_name] = instrument

    def add_function(self, function_name, function):
        self.functions.append((function_name, function))

    def get_instrument(self, instrument_name):
        return self.instruments[instrument_name]

    def get_function(self, function_name):
        for fn in self.functions:
            if fn[0] == function_name:
                return fn[1]

    def oscilloscope_control(self, instrument_name, command):
        instrument = self.get_instrument(instrument_name)
        instrument.write(command)
        waveform = instrument.query_ascii_values('WFMPRE:WFNR?')
        return waveform

    def function_generator_control(self, instrument_name, waveform, frequency, amplitude):
        instrument = self.get_instrument(instrument_name)
        instrument.write(f'SOUR1:FUNC {waveform}')
        instrument.write(f'SOUR1:FREQ {frequency}')
        instrument.write(f'SOUR1:VOLT {amplitude}')

    def multimeter_measure(self, instrument_name):
        instrument = self.get_instrument(instrument_name)
        measurement = instrument.query_ascii_values('MEAS?')
        return measurement

    def power_supply_control(self, instrument_name, voltage, current):
        instrument = self.get_instrument(instrument_name)
        instrument.write(f'APPLY {voltage}, {current}')

    def thermometer_measure(self, instrument_name):
        instrument = self.get_instrument(instrument_name)
        temperature = instrument.query_ascii_values('READ?')
        return temperature

    def frequency_counter_measure(self, instrument_name):
        instrument = self.get_instrument(instrument_name)
        frequency = instrument.query_ascii_values('MEAS:FREQ?')
        return frequency

    def spectrum_analyzer_measure(self, instrument_name, start_freq, stop_freq, num_points):
        instrument = self.get_instrument(instrument_name)
        instrument.write(f'SENSE:FREQ:STAR {start_freq}')
        instrument.write(f'SENSE:FREQ:STOP {stop_freq}')
        instrument.write(f'SENSE:SWE:POIN {num_points}')
        spectrum = instrument.query_ascii_values('TRAC1:DATA? TRACE1')
        return spectrum





# Ressourcenadresse des Geräts
resource = 'USB0::0xF4EC::0xEE3A::SPD1168XG8001931::INSTR'

# Visa-Ressourcenobjekt erstellen
rm = pyvisa.ResourceManager()
inst = rm.open_resource(resource)

# Spannung und Strom einstellen
inst.write('VOLT 3.3') # Setze die Spannung auf 3.3V
inst.write('CURR 0.5') # Setze den Strom auf 0.5A

# Ausgang einschalten
inst.write('OUTP ON')

# Visa-Ressourcenobjekt schließen
inst.close()
