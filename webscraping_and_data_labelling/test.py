import argparse

# parser = argparse.ArgumentParser(description="Process some integers.")
# parser.add_argument(
#     "integers", metavar="N", type=int, nargs="+", help="an integer for the accumulator"
# )
# parser.add_argument(
#     "--sum",
#     dest="accumulate",
#     action="store_const",
#     const=sum,
#     default=max,
#     help="sum the integers (default: find the max)",
# )

# args = parser.parse_args()
# print(args.accumulate(args.integers))

parser = argparse.ArgumentParser(description="BBC Pidgin Scraper")
parser.add_argument(
    "--output_file_name",
    type=str,
    default="bbc_pidgin_corpus.csv",
    help="Name of output file",
)

print(parser)
