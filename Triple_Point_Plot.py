import plotly.express as px
import numpy as np
####################################################


def fuc(t, c_1, c_2, poww):
    R = 8.314                       # Universal Gas constant
    del_g = c_1*t-c_2
    k = del_g/((R*t)*poww)
    f = np.exp(k)
    return 1/(1+f)                      # This Function Returns PH2/(pH2+ PH2O)


li_t = np.linspace(300, 1500, 100)       # Temperature in the range 300-1500k

####################################################

fig = px.scatter(x=li_t, y=fuc(li_t, 69.25, 64900, 1),)
fig.update_traces(marker=dict(size=7, color="blue"),
                  name=r"$Fe_3O_4 \ to \ FeO$", showlegend=True)
fig1 = px.scatter(x=li_t, y=fuc(li_t, 89.2, 101800, 4),)
fig1.update_traces(marker=dict(
    size=7, color="green"), name=r"$Fe_3O_4 \ to \ Fe$", showlegend=True)

fig2 = px.scatter(x=li_t, y=fuc(li_t, 6.65, 12300, 1),)
fig2.update_traces(marker=dict(
    size=7, color="red"), name=r"$FeO \ to \ Fe$", showlegend=True)
fig.add_trace(fig1.data[0])
fig.add_trace(fig2.data[0])
fig.update_layout(title=r'$Triple \ point \ for \  FeO, \  Fe, \ Fe_3O_4$',
                  xaxis_title=r'$Temperature(K)$',
                  yaxis_title=r'$\frac{P(H_2)}{P(H_2)+P(H_2O)}$', font=dict(family='Balto, sans-serif',
                                                                            size=20,
                                                                            color='rgb(37,37,37)'), margin=dict(
                      l=100,
                      b=100,
                      pad=4
                  ), legend=dict(
                      yanchor="bottom",
                      y=0.01,
                      xanchor="left",
                      x=0.01
                  ))

fig.add_annotation(text=r"Triple Point ~845K",
                   xref="paper", yref="paper",
                   x=0.35, y=0.59, showarrow=False, font=dict(family='Gravitas One, cursive',
                                                              size=20,
                                                              color='black'),)
fig.show()
