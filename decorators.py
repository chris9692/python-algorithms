def person_lister(f):
    def inner(people):
        people = sorted(people, key=lambda x: int(x[2]))
        return list([f(person) for person in people])
    return inner

@person_lister
def name_format(person):
    return ("Mr." if person[3] == "M" else "Ms.") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = ['Mike Thomson 20 M'.split(), 'Robert Bustle 32 M'.split(), 'Andria Bustle 30 F'.split()]
    print('\n'.join(name_format(people))) 

def phonewrapper(f):
    def wrap(phone_list):
          f(['+91 ' + p[-10:-5] + ' ' + p[-5:] for p in phone_list])
    return wrap          
    
@phonewrapper    
def sort_phone_list(phone_list):
    print('\n'.join(sorted(phone_list)))
    
if __name__ == '__main__':
    l = ['07895462130', '919875641230', '9195969878']
    sort_phone_list(l)
