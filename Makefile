FLAGS = --secret-file .env
ACT = act $(FLAGS)

test_print:
	$(ACT) -W test_integration/test_print/test_print.yml workflow_dispatch