from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, _tree

lisa = 1
irregular = 0
pera = 1
laranja = 0

pomar = [[120, lisa],[140, lisa],[180, irregular], [200, irregular]]

resultado = [pera, pera, laranja, laranja]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(pomar, resultado)

peso = 120
superficie = 1

resultadousu = clf.predict([[peso, superficie]])

if resultadousu == 1:
    print('Pera')
else:
    print('Laranja')