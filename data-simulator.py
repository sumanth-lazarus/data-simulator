import gym
import highway_env

import warnings
warnings.filterwarnings("ignore")

class HighwayEnvWrapper(gym.Env):
    def __init__(self):
        self.env = gym.make('highway-v0')
        self.observation_space = self.env.observation_space
        self.action_space = self.env.action_space
        self.env.configure({
            "duration": 3,
            "vehicles_count": 0,
            "simulation_frequency": 30,
        })
        print(self.env.config)

    def reset(self):
        return self.env.reset()

    def step(self, action):
        obs, reward, done, truncated, info = self.env.step(action)
        return obs, reward, done, truncated, info

    def render(self, mode='human'):
        return self.env.render(mode)




a = {'observation':
     {'type': 'Kinematics', 'vehicles_count': 15, 'features': ['presence', 'x', 'y', 'vx', 'vy', 'cos_h', 'sin_h'], 'features_range': {'x': [-100, 100], 'y': [-100, 100], 'vx': [-20, 20], 'vy': [-20, 20]}, 'absolute': True, 'flatten': False, 'observe_intentions': False}, 'action': {'type': 'DiscreteMetaAction', 'longitudinal': True, 'lateral': False, 'target_speeds': [0, 4.5, 9]}, 'simulation_frequency': 30, 'policy_frequency': 1, 'other_vehicles_type': 'highway_env.vehicle.behavior.IDMVehicle', 'screen_width': 600, 'screen_height': 600, 'centering_position': [0.5, 0.6], 'scaling': 7.15, 'show_trajectories': False, 'render_agent': True, 'offscreen_rendering': False, 'manual_control': False, 'real_time_rendering': False, 'duration': 3, 'destination': 'o1', 'controlled_vehicles': 1, 'initial_vehicle_count': 10, 'spawn_probability': 0.6, 'collision_reward': -5, 'high_speed_reward': 1, 'arrived_reward': 1, 'reward_speed_range': [7.0, 9.0], 'normalize_reward': False, 'offroad_terminal': False, 'vehicles_count': 0}

b = {'observation': {'type': 'Kinematics'}, 'action': {'type': 'DiscreteMetaAction'}, 'simulation_frequency': 30, 'policy_frequency': 1, 'other_vehicles_type': 'highway_env.vehicle.behavior.IDMVehicle', 'screen_width': 600, 'screen_height': 150, 'centering_position': [0.3, 0.5], 'scaling': 5.5, 'show_trajectories': False, 'render_agent': True, 'offscreen_rendering': False, 'manual_control': False, 'real_time_rendering': False, 'lanes_count': 4, 'vehicles_count': 0, 'controlled_vehicles': 1, 'initial_lane_id': None, 'duration': 3, 'ego_spacing': 2, 'vehicles_density': 1, 'collision_reward': -1, 'right_lane_reward': 0.1, 'high_speed_reward': 0.4, 'lane_change_reward': 0, 'reward_speed_range': [20, 30], 'normalize_reward': True, 'offroad_terminal': False}

c = {'observation': {'type': 'Kinematics', 'vehicles_count': 0, 'features': ['presence', 'x', 'y', 'vx', 'vy', 'cos_h', 'sin_h'], 'features_range': {'x': [-100, 100], 'y': [-100, 100], 'vx': [-20, 20], 'vy': [-20, 20]}, 'absolute': True, 'flatten': False, 'observe_intentions': False}, 'action': {'type': 'DiscreteMetaAction', 'longitudinal': True, 'lateral': False, 'target_speeds': [0, 4.5, 9]}, 'simulation_frequency': 30, 'policy_frequency': 1, 'other_vehicles_type': 'highway_env.vehicle.behavior.IDMVehicle', 'screen_width': 600, 'screen_height': 600, 'centering_position': [0.5, 0.6], 'scaling': 7.15, 'show_trajectories': False, 'render_agent': True, 'offscreen_rendering': False, 'manual_control': False, 'real_time_rendering': False, 'duration': 3, 'destination': 'o1', 'controlled_vehicles': 1, 'initial_vehicle_count': 10, 'spawn_probability': 0.6, 'collision_reward': -5, 'high_speed_reward': 1, 'arrived_reward': 1, 'reward_speed_range': [7.0, 9.0], 'normalize_reward': False, 'offroad_terminal': False}