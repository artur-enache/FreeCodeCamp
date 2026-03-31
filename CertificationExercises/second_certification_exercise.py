"""https://www.freecodecamp.org/learn/python-v9/lab-budget-app/build-a-budget-app"""

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append(dict([('amount', amount), ('description', description)]))

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append(dict([('amount', -abs(amount)), ('description', description)]))
            return True
        else:
            return False

    def check_funds(self, amount):
        balance = sum(item['amount'] for item in self.ledger)
        return amount <= balance

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category_instance):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount, f'Transfer to {category_instance.name}')
            category_instance.deposit(amount, f'Transfer from {self.name}')
            return True

    def __str__(self):
        output = ''
        title_length = 30
        category_length = len(self.name)
        no_of_asterisks = title_length - category_length
        title = f"{'*' * (no_of_asterisks // 2)}{self.name}{'*' * (no_of_asterisks // 2)}\n"
        output += title
        for line in self.ledger:
            description = line['description'][:23]
            amount = f"{line['amount']:.2f}"[:7]
            output += f'{description:<23}{amount:>7}\n'
        output += f'Total: {self.get_balance()}'
        return output

def create_spend_chart(categories):
    category_sums = {}
    category_dots = {}
    category_lines = {}
    category_labels = {}
    total_sums = 0
    labels_y = [ f'{str(i):>3}| ' for i in range(0, 101, 10) ]

    max_length = max(len(c.name) for c in categories)

    for category in categories:
        category_sums[category.name] = sum(item['amount'] for item in category.ledger if item['amount'] < 0)

    for key, value in category_sums.items():
        total_sums -= value
    total_sums = round(total_sums, 2)

    for key, value in category_sums.items():
        category_dots[key] = int(abs(value / total_sums * 100) // 10)

    for k, v in category_dots.items():
        category_labels[k] = f'{k:<{max_length}}'

    for key, value in category_dots.items():
        category_lines[key] = f'{"o" * (value + 1):<11}'

    output = 'Percentage spent by category\n'
    for i in range(10, -1, -1):
        output += labels_y[i]
        for line in category_lines.values():
            output += f'{line[i]:<3}'
        output += '\n'
    output += '    ' + ( '---' *  (len(category_lines))) + '-\n'

    lines = []
    individual_line = ''

    for i in range(0, max_length):
        for key, value in category_labels.items():
            individual_line += f'{value[i]}  '
        lines.append(individual_line)
        individual_line = ''

    new_lines = []

    for line in lines:
        new_line = '     ' + line
        new_lines.append(new_line)

    output += '\n'.join(new_lines)
    return output


def main():
    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.99, 'groceries')
    clothing = Category('Clothing')
    clothing.deposit(200, 'initial deposit')
    clothing.withdraw(105.55, 'Pyjamas')
    transport = Category('Transport')
    transport.deposit(200, 'initial deposit')
    transport.withdraw(33.4, 'Bus tickets')
    print(create_spend_chart([food, clothing, transport]))

if __name__ == '__main__':
    main()