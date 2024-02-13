# collectStrings
# Write a function called collectStrings which accepts an object and returns an array of all the values in the object that have a typeof string.

# Examples

# obj = {
#   "stuff": 'foo',
#   "data": {
#     "val": {
#       "thing": {
#         "info": 'bar',
#         "moreInfo": {
#           "evenMoreInfo": {
#             "weMadeIt": 'baz'
#           }
#         }
#       }
#     }
#   }
# }
 
# collectStrings(obj) # ['foo', 'bar', 'baz']


def collectStrings(obj):
    resultArr = []
    for key in obj:
        if type(obj[key]) is str:
            resultArr.append(obj[key])
        if type(obj[key]) is dict:
            resultArr = resultArr + collectStrings(obj[key])
    return resultArr