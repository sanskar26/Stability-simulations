import plotly.express as px
import numpy as np
####################################################


def fuc(t, c_1, c_2, poww):
    R = 8.314                          # Universal Gas constant
    del_g = c_1*t-c_2
    k = del_g/((R*t)*poww)
    f = np.exp(k)                       # This Function Returns PH2/(pH2+ PH2O)
    return 1/(1+f)


li_t1 = np.linspace(300, 845, 50)       # Temperature in the range 300-845k


li_t2 = np.linspace(845, 1500, 50)  # Temperature in the range 845-1500k

####################################################

fig = px.scatter(x=li_t2, y=fuc(li_t2, 69.25, 64900, 1),)
fig.update_traces(marker=dict(size=7, color="blue"),
                  name=r"$Fe_3O_4 \ to \ FeO$", showlegend=True)
fig1 = px.scatter(x=li_t1, y=fuc(li_t1, 89.2, 101800, 4),)
fig1.update_traces(marker=dict(
    size=7, color="green"), name=r"$Fe_3O_4 \ to \ Fe$", showlegend=True)

fig2 = px.scatter(x=li_t2, y=fuc(li_t2, 6.65, 12300, 1),)
fig2.update_traces(marker=dict(
    size=7, color="red"), name=r"$FeO \ to \ Fe$", showlegend=True)
fig.add_trace(fig1.data[0])
fig.add_trace(fig2.data[0])
fig.update_layout(title=r'$Stability \ In \ Different \ Region$',
                  xaxis_title=r'$Temperature(K)$',
                  yaxis_title=r'$\frac{P(H_2)}{P(H_2)+P(H_2O)}$', font=dict(family='Balto, sans-serif',
                                                                            size=20,), legend=dict(
                      yanchor="bottom",
                      y=0.01,
                      xanchor="left",
                      x=0.01
                  ), margin=dict(
                      l=100,
                      b=100,
                      pad=4
                  ), paper_bgcolor="#fafafa",)


fig.add_annotation(text=r"$Fe_3O_4 $",
                   xref="paper", yref="paper",
                   x=0.25, y=0.45, showarrow=False, font=dict(family='Gravitas One, cursive',
                                                              size=25,
                                                              color='black'),)

fig.add_annotation(text=r"$FeO $",
                   xref="paper", yref="paper",
                   x=0.75, y=0.35, showarrow=False, font=dict(family='Gravitas One, cursive',
                                                              size=25,
                                                              color='black'),)

fig.add_annotation(text=r"$Fe $",
                   xref="paper", yref="paper",
                   x=0.75, y=0.85, showarrow=False, font=dict(family='Gravitas One, cursive',
                                                              size=25,
                                                              color='black'),)

fig.show()
