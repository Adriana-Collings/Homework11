from enum import Enum
import InputData as Data
import scr.MarkovClasses as MarkovCls


class HealthStats(Enum):
    """ health states of patients with HIV """
    WELL = 0
    STROKE = 1
    POST_STROKE = 2
    STOKE_DEATH = 3
    NON_STROKE_DEATH = 4


class Therapies(Enum):
    """ mono vs. combination therapy """
    NONE = 0
    ANTICOAG = 1


class ParametersFixed():
    def __init__(self, therapy):

        # selected therapy
        self._therapy = therapy

        # simulation time step
        self._delta_t = Data.DELTA_T

        self._adjDiscountRate = Data.DISCOUNT * Data.DELTA_T

        # initial health state
        self._initialHealthState = HealthStats.WELL

        # annual treatment cost
        if self._therapy == Therapies.NONE:
            self._annualTreatmentCost = 0
        if self._therapy == Therapies.ANTICOAG:
            self._annualTreatmentCost = Data.Anticoag_COST

        # transition probability matrix of the selected therapy
        self._prob_matrix = []
        # treatment relative risk
        self._treatmentRR = 0

        # calculate transition probabilities depending of which therapy options is in use
        if therapy == Therapies.NONE:
            self._prob_matrix = add_background_mortality(prob_matrix=Data.RATE_MATRIX)
        else:
            self._prob_matrix = add_background_mortality(prob_matrix=Data.RATE_TREAT) # calculate_prob_matrix_anticoag()

        self._annualStateCosts = Data.HEALTH_COST
        self._annualStateUtilities = Data.HEALTH_UTILITY

    def get_initial_health_state(self):
        return self._initialHealthState

    def get_delta_t(self):
        return self._delta_t

    def get_adj_discount_rate(self):
        return self._adjDiscountRate

    def get_transition_prob(self, state):
        return self._prob_matrix[state.value]

    def get_annual_state_cost(self, state):
        if state == HealthStats.STOKE_DEATH or HealthStats.NON_STROKE_DEATH:
            return 0
        else:
            return self._annualStateCosts[state.value]

    def get_annual_state_utility(self, state):
        if state == HealthStats.STOKE_DEATH or HealthStats.NON_STROKE_DEATH:
            return 0
        else:
            return self._annualStateUtilities[state.value]

    def get_annual_treatment_cost(self):
        return self._annualTreatmentCost

def add_background_mortality(prob_matrix):

    # find the transition rate matrix
    rate_matrix = Data.RATE_MATRIX  # MarkovCls.discrete_to_continuous(prob_matrix, 1)
    # add mortality rates
    #for s in HealthStats:
        # add background rates to non-death states (background mortality rate for death-state is assumed 0)
     #   if s not in [HealthStats.HIV_DEATH, HealthStats.BACKGROUND_DEATH]:
      #      rate_matrix[s.value][HealthStats.BACKGROUND_DEATH.value] \
       #         = -np.log(1 - Data.ANNUAL_PROB_BACKGROUND_MORT)

    # convert back to transition probability matrix
    prob_matrix[:], p = MarkovCls.continuous_to_discrete(rate_matrix, Data.DELTA_T)
    # print('Upper bound on the probability of two transitions within delta_t:', p)
    return prob_matrix

