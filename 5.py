for i in range(0,5):
    print("*"*i)
#Simple Star Pattern Program


#problem 24
import itertools

def compute():
	arr = list(range(10))
	temp = itertools.islice(itertools.permutations(arr), 999999, None)
	return "".join(str(x) for x in next(temp))


if __name__ == "__main__":
	print(compute())
