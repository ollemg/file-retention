create-files:
	mkdir -p /tmp/create_files/{a,b,c}/{b,c,d}/{c,d,e}/{d,e,f}
	touch /tmp/create_files/{a,b,c}/{b,c,d}/{c,d,e}/{d,e,f}/arquivo{1..5}.{md,txt,ini}
	touch /tmp/create_files/{a,b,c}/{b,c,d}/{c,d,e}/arquivo{1..5}.{md,txt,ini}
	touch /tmp/create_files/{a,b,c}/{b,c,d}/arquivo{1..5}.{md,txt,ini}
	touch /tmp/create_files/{a,b,c}/arquivo{1..5}.{md,txt,ini}
	touch /tmp/create_files/arquivo{1..5}.{md,txt,ini}

create-files-shorts:
	mkdir -p /tmp/create_files/{a,b,c}/{b,c,d}/
	touch /tmp/create_files/{a,b,c}/{b,c,d}/arquivo{1..3}.{md,txt,ini}
	touch /tmp/create_files/{a,b,c}/arquivo{1..3}.{md,txt,ini}
	touch /tmp/create_files/arquivo{1..3}.{md,txt,ini}

create-files-test:
	mkdir -p /tmp/create_files/{a,b,c}/{b,c,d}/
	touch /tmp/create_files/{a,b,c}/{b,c,d}/arquivo1.{md,txt,ini}
	touch /tmp/create_files/{a,b,c}/arquivo1.{md,txt,ini}
	touch /tmp/create_files/arquivo1.{md,txt,ini}

mail-server:
	sudo python3 -m smtpd -c DebuggingServer -n localhost:25

lint:
	black -l 79 ./file_retention

test:
	make create-files-test
	python3 -m file_retention snapshot /tmp/create_files/ -e txt
	@echo "##################"
	python3 -m file_retention snapshot /tmp/create_files/ -e aaa
	@echo "################## delete -r 0"
	python3 -m file_retention delete -r 0
	@echo "################## delete -r 100"
	python3 -m file_retention delete -r 100
	@echo "##################"
	python3 -m file_retention delete -r 100 -y
	@echo "##################"
	python3 -m file_retention delete -r 0 -y
	@echo "##################"
	python3 -m file_retention mail ~/.file_retention/mail.yml -r 0
	@echo "##################"
	python3 -m file_retention mail ~/.file_retention/2022-01-26.yml -r 0
	@echo "##################"