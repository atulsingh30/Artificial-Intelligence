import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

traffic_flow = ctrl.Antecedent(np.arange(500, 3000, 1), 'traffic flow')
traffic_flow['low'] = fuzz.trimf(traffic_flow.universe, [500, 1000, 1500])
traffic_flow['medium'] = fuzz.trimf(traffic_flow.universe, [1000, 2000, 2500])
traffic_flow['high'] = fuzz.trimf(traffic_flow.universe, [2000, 2500, 3000])

congestion = ctrl.Antecedent(np.arange(0, 1, 0.01), 'congestion')
congestion.automf(3)

speed = ctrl.Antecedent(np.arange(0, 100, 0.1), 'speed')
speed['slow'] = fuzz.trimf(speed.universe, [0, 20, 40])
speed['moderate'] = fuzz.trimf(speed.universe, [20, 50, 80])
speed['fast'] = fuzz.trimf(speed.universe, [60, 80, 100])

control_strategy = ctrl.Consequent(np.arange(0, 1, 0.01), 'control strategy')
control_strategy.automf(3)
rules = [
    ctrl.Rule(traffic_flow['low'] | congestion['low'], control_strategy['low']),
    ctrl.Rule(traffic_flow['medium'] & congestion['low'] & speed['slow'], control_strategy['low']),
    ctrl.Rule(traffic_flow['medium'] & congestion['low'] & speed['moderate'], control_strategy['mid']),
    ctrl.Rule(traffic_flow['medium'] & congestion['low'] & speed['fast'], control_strategy['high']),
    ctrl.Rule(traffic_flow['medium'] & congestion['mid'] & speed['slow'], control_strategy['low']),
    ctrl.Rule(traffic_flow['medium'] & congestion['mid'] & speed['moderate'], control_strategy['mid']),
    ctrl.Rule(traffic_flow['medium'] & congestion['mid'] & speed['fast'], control_strategy['high']),
    ctrl.Rule(traffic_flow['high'] & congestion['high'], control_strategy['high'])
]

control_system = ctrl.ControlSystem(rules)
sim = ctrl.ControlSystemSimulation(control_system)

sim.input['traffic flow'] = 1500
sim.input['congestion'] = 0.3
sim.input['speed'] = 65

sim.compute()
print(sim.output['control strategy'])