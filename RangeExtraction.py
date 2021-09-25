# The following is my solution
# I've added this file as I wanted to show the difference between good and bad code
# What I've written is a mess that was created through trial and error
# What I should have done is clean it up after I was done
# Regardless, my way led to nearly 90 lines of code
# I might add a demo video to explain how this works because honestly it's exhausting just looking at this mess
# There's a better solution at the bottom
def solution(x):
    count=0
    range=0
    y=[]
    index = 0
    for i in x:
        index = index + 1
        if index < len(x):
            range = i - x[index]
            if range == -1:
                count+=1
            else:
                if count == 0:
                    m = str(i)
                    y.append(m)
                elif count == 1:
                    m = str(x[index-2])
                    y.append(m)
                    m = str(i)
                    y.append(m)
                    count=0
                    range=0
                else:
                    m = str(x[index-count-1])
                    m = f'{m}-{str(x[index-1])}'
                    y.append(m)
                    count=0
                    range=0
        else:
            #range = x[index-3] - x[index-2]
            #print(index)
            range = x[index-2] - i
            #print(x[index-2])
            #print(range)
            #print(count)
            xrange = x[index-3] - x[index-2]
            if xrange == -1:
                if range == -1:
                    count+=1
                    if count == 1:
                        m = str(i)
                        y.append(m)
                    else:
                        m = str(x[index-count])
                        m = f'{m}-{str(i)}'
                        y.append(m)
                else:
                    if count == 0:
                        m = str(i)
                        y.append(m)
                    else:
                        m = str(x[index-count])
                        m = f'{m}-{str(i)}'
                        y.append(m)
            else:
                if range == -1:
                    if count == 1:
                        m = str(x[index-2])
                        y.append(m)
                        m = str(i)
                        y.append(m)
                else:
                    m=str(x[index-2])
                    y.append(m)
                    m=str(i)
                    y.append(m)
    index=0
    for op in y:
        if y.count(op) > 1:
            y.pop(index)
        index+=1

    f=''
    index=0
    for j in y:
        if index == 0:
            f+=str(j)
        else:
            if index <len(y):
                f+=','
                f+=str(j)
        index+=1
    return f

print(solution([-4,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
print(solution([1,2,3,4,5,7,8]))
print(solution([-88,-85,-83,-81,-78,-77,-75,-73,-71,-69,-67]))

# This is a better solution
# The reason for this is that its concise and more thought was put into the process before any code was written
# My tips for a situation like this is to write pseudocode
# If you know what you have to do and in what order, it is much easier to put that thought into code

def solutionz(args):
    out = []
    beg = end = args[0]

    for n in args[1:] + [""]:
        if n != end + 1:
            if end == beg:
                out.append( str(beg) )
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append( str(beg) + "-" + str(end) )
            beg = n
        end = n

    return ",".join(out)

print(solutionz([-4,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
print(solutionz([1,2,3,4,5,7,8]))
print(solutionz([-88,-85,-83,-81,-78,-77,-75,-73,-71,-69,-67]))
