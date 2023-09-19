import tests

if __name__ == "__main__":
	fails = tests.test_all()
	for epic_fail in fails:
		print(str(epic_fail))


def my_func():
	return 13