from typing import List
import numpy as np
import feature

class Selector:
    def __init__(self, candidates: List[str]):
        self.candidates = candidates
        self.dv_measurable_features = []
        self.ndv_measurable_features = []
        self.immeasurable_features = []
        self.accumulated_weight = 0


    def add_immeasurable_feature(self, feature: feature.Feature, expert_scores: List[int]):
        """ Adds a new immeasurable feature to the selector 
            Args: 
                feature (Feature): an instance of Feature class
                expert_scores (list[int]): expert score (0-4) assigned to each candidate
        """
        if len(self.candidates) != len(expert_scores):
            raise ValueError('the length of candidates and expert_scores can not be different')
        for expert_score in expert_scores:
            if expert_score < 0 or expert_score > 4:
                raise ValueError('expert score must be a value between 0 and 4')
        feature.values = expert_scores
        self.immeasurable_features.append(feature)

    def add_dv_measurable_feature(self, feature: feature.Feature, desired_value: float, mode: feature.Mode, values: List[float]):
        """ Adds a new measurable value feature with a desired value
            Args:
                feature (Feature): an instance of Feature class
                desired_value (float): a desired value to the feature
                mode (Feature.Mode): defines if it is maximizing or minimizing value
                values (List[float]): values assigned to each candidate 
        """
        feature.desired_value = desired_value
        feature.mode = mode
        if len(self.candidates) != len(values):
            raise ValueError('the length of candidates and values can not be different')
        feature.values = values
        self.dv_measurable_features.append(feature)
    
    def add_ndn_measurable_feature(self, feature: feature.Feature, mode: feature.Mode, values):
        """ Adds a new measurable value feature without a desired value
            Args:
                feature (Feature): an instance of Feature class
                mode (Feature.Mode): defines if it is maximizing or minimizing value
                values (List[float]): values assigned to each candidate 
        """
        feature.mode = mode
        if len(self.candidates) != len(values):
            raise ValueError('the length of candidates and values can not be different')
        feature.values = values
        self.ndv_measurable_features.append(feature)

    def __calc_accumulated_weights(self):
        for f in self.immeasurable_features:
            self.accumulated_weight = self.accumulated_weight + f.weight
        for f in self.dv_measurable_features:
            self.accumulated_weight = self.accumulated_weight + f.weight
        for f in self.ndv_measurable_features:
            self.accumulated_weight = self.accumulated_weight + f.weight

    def calc_premium_values(self):
        self.__calc_accumulated_weights()
        premium_values = np.zeros(len(self.candidates))
        # calc premium values to the immeasurable features
        for f in self.immeasurable_features:
            index = 0
            for expert_score in f.values:
                premium_values[index] = premium_values[index] + (f.weight/self.accumulated_weight) * (expert_score * 0.25)
                index = index + 1
        # calc premium values to the measurable features with desired value
        for f in self.dv_measurable_features:
            index = 0
            normalization_factor = f.desired_value
            for value in f.values:
                score = 0
                if f.mode == feature.Mode.MINIMAZING:
                    score = normalization_factor/value
                else:
                    score = value/normalization_factor
                premium_values[index] = premium_values[index] + (f.weight/self.accumulated_weight) * score
                index = index + 1
        # calc premium values to the measurable features without desired value
        for f in self.ndv_measurable_features:
            index = 0
            normalization_factor = 0
            if f.mode == feature.Mode.MINIMAZING:
                normalization_factor = np.min(f.values)
            else:
                normalization_factor = np.max(f.values)
            for value in f.values:
                score = 0
                if f.mode == feature.Mode.MINIMAZING:
                    score = normalization_factor/value
                else:
                    score = value/normalization_factor
                premium_values[index] = premium_values[index] + (f.weight/self.accumulated_weight) * score
                index = index + 1
        index = 0
        for cadidate in self.candidates:
            print(cadidate, ": ", round(premium_values[index],3))
            index = index + 1