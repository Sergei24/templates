import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

path = '/home/username/fantasy.ttf' # way to downloaded new font (especially for cyrillic fonts)
prop = font_manager.FontProperties(fname=path)
mpl.rcParams['font.family'] = prop.get_name()

fig, ax = plt.subplots()
ax.set_title('Test text', fontproperties=prop, size=40)
