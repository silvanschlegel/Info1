#-- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

def all_truthy(values):
    if values == []:
        return True
    for i in values:
        if i == False:
            return False
    return True

#-- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

### DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
assert(all_truthy([True, "yes", "no", 1, [{}]]))
assert(all_truthy([]))
assert(not all_truthy([True, "yes", 0.0]))