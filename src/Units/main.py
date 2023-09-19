import tests

if __name__ == "__main__":
	fails = tests.test_all()
	for epic_fail in fails:
		print(epic_fail)


def my_func():
	return 13