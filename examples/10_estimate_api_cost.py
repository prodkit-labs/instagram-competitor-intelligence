from common import load_usernames, parser


PLAN_COSTS = {
    "start": 0.02,
    "standard": 0.001,
    "business": 0.00069,
    "ultra": 0.0006,
}


arg_parser = parser("Estimate rough API request usage and monthly cost")
arg_parser.add_argument("--runs-per-month", type=int, default=30)
arg_parser.add_argument("--requests-per-account", type=int, default=2)
arg_parser.add_argument("--plan", choices=PLAN_COSTS.keys(), default="standard")
args = arg_parser.parse_args()

accounts = load_usernames(args.accounts)
monthly_requests = len(accounts) * args.requests_per_account * args.runs_per_month
cost = monthly_requests * PLAN_COSTS[args.plan]

print(f"Accounts: {len(accounts)}")
print(f"Runs per month: {args.runs_per_month}")
print(f"Requests per account per run: {args.requests_per_account}")
print(f"Estimated monthly requests: {monthly_requests:,}")
print(f"Plan: {args.plan} (${PLAN_COSTS[args.plan]} per request)")
print(f"Estimated monthly API cost: ${cost:,.2f}")
