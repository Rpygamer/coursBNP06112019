from argparse import ArgumentParser


parser = ArgumentParser(
    description="Dit bonjour à quelqu'un",
)

parser.add_argument("iteration", help="nombre d'itérations", type=int)
parser.add_argument("-n", "--name", help="prenom de la personne")
parser.add_argument("-l", "--lastname", help="nom de la personne")

args = parser.parse_args()

for i in range(args.iteration):
    print(f"Bonjour {args.name}")
