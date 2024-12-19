import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_register(line: str) -> int:
    return int(line.split(":")[1])


def parse_program(line: str) -> list[int]:
    content = line.split(":")[1].strip().split(",")

    return [int(item) for item in content]


class Computer:
    def __init__(self, register_a, register_b, register_c, program):
        self.__register_a = register_a
        self.__register_b = register_b
        self.__register_c = register_c
        self.__program = program
        self.__instruction_pointer = 0
        self.__output = []

    def __handle_combo_operand(self, operand) -> int:
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return self.__register_a
        elif operand == 5:
            return self.__register_b
        elif operand == 6:
            return self.__register_c
        else:
            raise Exception("Should not happen")

    def run_program(self):
        while self.__instruction_pointer <= len(self.__program) - 2:
            opcode = self.__program[self.__instruction_pointer]
            operand = self.__program[self.__instruction_pointer + 1]
            has_jumped = False

            if opcode == 0:
                numerator = self.__register_a
                denominator = 2 ** self.__handle_combo_operand(operand)

                self.__register_a = numerator // denominator
            elif opcode == 1:
                self.__register_b = self.__register_b ^ operand
            elif opcode == 2:
                self.__register_b = self.__handle_combo_operand(operand) % 8
            elif opcode == 3:
                if self.__register_a != 0:
                    has_jumped = True
                    self.__instruction_pointer = operand
            elif opcode == 4:
                self.__register_b = self.__register_b ^ self.__register_c
            elif opcode == 5:
                output = self.__handle_combo_operand(operand) % 8

                self.__output.append(output)
            elif opcode == 6:
                numerator = self.__register_a
                denominator = 2 ** self.__handle_combo_operand(operand)

                self.__register_b = numerator // denominator
            elif opcode == 7:
                numerator = self.__register_a
                denominator = 2 ** self.__handle_combo_operand(operand)

                self.__register_c = numerator // denominator

            if not has_jumped:
                self.__instruction_pointer += 2

    def get_output(self):
        return self.__output


if __name__ == "__main__":
    lines = read_input()

    register_a = parse_register(lines[0])
    register_b = parse_register(lines[1])
    register_c = parse_register(lines[2])

    program = parse_program(lines[4])

    computer = Computer(register_a, register_b, register_c, program)
    computer.run_program()

    output = computer.get_output()

    print(','.join(str(item) for item in output))

