namespace = [{'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'}]
print(namespace)
namespace[2]['lion'] = 'orange'
namespace[0]['snake'] = 'red'
#del namespace[1]
namespace[1].clear()
print(namespace)

