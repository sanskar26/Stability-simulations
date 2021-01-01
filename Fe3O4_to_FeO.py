import plotly.express as px
import numpy as np
####################################################
# del_g = 69.25T - 64900


def fuc(t, c_1, c_2, poww):
    R = 8.314                           # Universal Gas constant
    del_g = c_1*t-c_2
    k = del_g/((R*t)*poww)
    f = np.exp(k)                       # This Function Returns PH2/(pH2+ PH2O)
    return 1/(1+f)


li_t = np.linspace(300, 1500, 100)        # Temperature in the range 300-1500k

####################################################

fig = px.scatter(x=li_t, y=fuc(li_t, 69.25, 64900, 1),)
fig.update_traces(marker=dict(size=10, color="blue"),
                  name=r"$Fe_3O_4 \ to \ FeO  $ ", showlegend=True)

fig.update_layout(title=r'$Stability \ Curve \ For \ Fe_3O_4 \ and \ FeO$',
                  xaxis_title=r'$Temperature(K)$',
                  yaxis_title=r'$\frac{P(H_2)}{P(H_2)+P(H_2O)}$', font=dict(family='Balto, sans-serif',
                                                                            size=20,
                                                                            color='rgb(37,37,37)'), margin=dict(
                      l=100,
                      b=100,

                  ), legend=dict(
                      yanchor="top",
                      y=1,
                      xanchor="right",
                      x=1
                  ))

fig.add_annotation(text=r"$Fe_3O_4 \ is \ stable$",
                   xref="paper", yref="paper",
                   x=0.25, y=0.20, showarrow=False, font=dict(family='Gravitas One, cursive',
                                                              size=20,
                                                              color='MidnightBlue'))
fig.add_annotation(text=r"$FeO \ is \ stable$",
                   xref="paper", yref="paper",
                   x=0.85, y=0.65, showarrow=False, font=dict(family='Gravitas One, cursive',
                                                              size=20,
                                                              color='MidnightBlue'))


fig.add_annotation(text="Region I",
                   xref="paper", yref="paper",
                   x=0.8, y=0.82, showarrow=False, font=dict(family='Gravitas One, cursive',
                                                             size=25,
                                                             color='crimson'), bgcolor="LightSalmon")


fig.add_annotation(text="Region II",
                   xref="paper", yref="paper",
                   x=0.25, y=0.35, showarrow=False, font=dict(family='Gravitas One, cursive',
                                                              size=25,
                                                              color='crimson'), bgcolor="LightSalmon")
fig.show()
