import monte_carlo as mc

if __name__ == "__main__":
    equation_parser = argparse.ArgumentParser(add_help=False)
    equation_parser.add_argument("equation","-e", type=str, help="math equation", action='store_const')

    integral_parser = argparse.ArgumentParser(parents=[equation_parser])
    parser.add_argument("--integral")
    args = parser.parse_args();
