CC = gcc
CFLAG = -Wall -pedantic -Werror -Wextra -std=gnu89
SRC = main.c free_dlistint.c print_dlistint.c add_dnodeint_end.c delete_dnodeint_at_index.c
OBJ = $(SRC:.c=.o)
NAME = delete_dnodeint
RM = rm -f

.PHONY: all clean oclean fclean re

all: lists.h $(OBJ)
	$(CC) $(OBJ) -o $(NAME)

clean:
	$(RM) *~ $(NAME)

oclean:
	$(RM) $(OBJ)

fclean: clean oclean

re: fclean all
