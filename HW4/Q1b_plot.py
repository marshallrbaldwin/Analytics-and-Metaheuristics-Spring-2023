# -*- coding: utf-8 -*-
"""
@author: Marshall Baldwin
"""
from matplotlib import pyplot as plt
risk_return_tuples = [(0.0, 1191016.0),
                      (9628.947368, 1256492.842105),
                      (19257.894737, 1321969.684211),
                      (28886.842105, 1387446.526316),
                      (38515.789474, 1448855.050316),
                      (48144.736842, 1475767.187895),
                      (57773.684211, 1502679.325474),
                      (67402.631579, 1529591.463053),
                      (77031.578947, 1556503.600632),
                      (86660.526316, 1583415.738211),
                      (96289.473684, 1610327.875789),
                      (105918.421053, 1636193.777057),
                      (115547.368421, 1657853.178636),
                      (125176.315789, 1679512.580214),
                      (134805.263158, 1701171.981793),
                      (144434.210526, 1722831.383371),
                      (154063.157895, 1744490.78495),
                      (163692.105263, 1766150.186528),
                      (173321.052632, 1785752.283922),
                      (182950.0, 1797600.0)]

risks = [i[0] for i in risk_return_tuples]
returns = [i[1]-1_000_000 for i in risk_return_tuples]

fig, ax = plt.subplots(1, figsize = (6,4), dpi = 200)
ax.plot(risks, returns, marker = 'o', ms = 4., c = "black", ls = "--")
ax.fill_between(risks, returns, 170000, color = 'grey', alpha = .3)
ax.set_title("Risk vs. Return on $1M Investment")
ax.set_xlabel("Risk Score")
ax.set_ylabel("ROI [$]")
ax.set_ylim(170000, None)
ax.set_xlim(None, 190000)
fig.text(.6,.28,"Feasible Region")
fig.text(.5,.51,"Pareto Front", rotation = 28)
fig.text(.3, .8,"Infeasible Region")
ax.grid()
fig.tight_layout()