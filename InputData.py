POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 15   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1/52         # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03

# transition matrix
TRANS_MATRIX = [
    [0.75,  0.15,   0.0,    0.1],   # Well
    [0,     0.0,    1.0,    0.0],   # Stroke
    [0,     0.25,   0.55,   0.2],   # Post-Stroke
    [0.0,   0.0,    0.0,    1.0],   # Dead
    ]

RATE_MATRIX = [
    [None, 0.0136, 0, 0.0151, 0.0178],
    [0, None, 52, 0, 0],
    [0, 0.00040852, None, 0.00010213, 0.0178],
    [0, 0, 0, None, 0],
    [0, 0, 0, 0, None]
    ]

RATE_TREAT = [
    [None, 0.0136, 0, 0.0151, 0.0178],
    [0, None, 52, 0, 0],
    [0, 0.00030639, None, 0.00010213, 0.01869],
    [0, 0, 0, None, 0],
    [0, 0, 0, 0, None]
]

# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
RR_STROKE = 0.65
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
RR_BLEEDING = 1.05

HEALTH_UTILITY = [
    1,  # well
    0.2,  # stroke
    0.9,  # post-stroke
    0,  # dead (stroke)
    0  # dead (Non stroke)
]

HEALTH_COST = [
    0,
    5000,  # stroke
    200,  # post-stroke /year
    0
]

HEALTH_COST_TREAT = [
    0,
    5000,
    750,
    0,
    0
]

Anticoag_COST = 2000