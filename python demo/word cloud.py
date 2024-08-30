import wordcloud
t = 'makeblock AI STEAM mBot Ranger Ultimate Codey halocode mBlock Neuron Laserbox'  #设置你要输出的内容
w = wordcloud.WordCloud(background_color='white',width = 1000,height = 1000)  #设置词云的生成格式
w.generate(t)  #选择词云要生成的文本
w.to_file('wordcloud.png')  #保存至本地文件，设置文件名称