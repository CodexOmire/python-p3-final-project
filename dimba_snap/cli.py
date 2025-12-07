import click
from datetime import datetime
from .services.user_service import create_user, list_users
from .services.team_service import create_team, list_teams
from .services.pitch_service import create_pitch, list_pitches
from .services.reservation_service import create_reservation, list_reservations
from .services.payment_service import add_payment, list_payments
from .db import Base, engine
import dimba_snap.models


@click.group()
def cli():
    pass


@click.group()
def user():
    pass


@click.group()
def team():
    pass


@click.group()
def pitch():
    pass


@click.group()
def reservation():
    pass


@click.group()
def payment():
    pass


cli.add_command(user)
cli.add_command(team)
cli.add_command(pitch)
cli.add_command(reservation)
cli.add_command(payment)


@user.command("add")
def add_user():
    name = click.prompt("Enter name")
    email = click.prompt("Enter email")
    role = click.prompt("Role (admin/team_manager)")
    try:
        u = create_user(name, email, role)
        click.echo(f"User created: {u.id} - {u.name}")
    except Exception as e:
        click.echo(f"Error: {e}")


@user.command("list")
def list_user_cmd():
    for u in list_users():
        click.echo(f"{u.id}: {u.name} ({u.email})")


@team.command("add")
def add_team():
    name = click.prompt("Team name")
    user_id = click.prompt("Manager user_id", type=int)
    try:
        t = create_team(name, user_id)
        click.echo(f"Team created: {t.id}")
    except Exception as e:
        click.echo(f"Error: {e}")


@team.command("list")
def list_team_cmd():
    for t in list_teams():
        click.echo(f"{t.id}: {t.name} (user {t.user_id})")


@pitch.command("add")
def add_pitch_cmd():
    name = click.prompt("Pitch name")
    location = click.prompt("Location")
    rate = click.prompt("Hourly rate", type=float)
    p = create_pitch(name, location, rate)
    click.echo(f"Pitch created: {p.id}")


@pitch.command("list")
def list_pitch_cmd():
    for p in list_pitches():
        click.echo(f"{p.id}: {p.name} - {p.location}")


@reservation.command("add")
def add_res_cmd():
    team_id = click.prompt("Team ID", type=int)
    pitch_id = click.prompt("Pitch ID", type=int)
    date_str = click.prompt("Date (YYYY-MM-DD)")
    start_str = click.prompt("Start time (HH:MM)")
    end_str = click.prompt("End time (HH:MM)")

    date = datetime.strptime(date_str, "%Y-%m-%d").date()
    start = datetime.strptime(start_str, "%H:%M").time()
    end = datetime.strptime(end_str, "%H:%M").time()

    try:
        r = create_reservation(team_id, pitch_id, date, start, end)
        click.echo(f"Reservation created: {r.id}")
    except Exception as e:
        click.echo(f"Error: {e}")


@reservation.command("list")
def list_res_cmd():
    for r in list_reservations():
        click.echo(f"{r.id}: team {r.team_id} pitch {r.pitch_id} on {r.date}")


@payment.command("add")
def add_pay_cmd():
    reservation_id = click.prompt("Reservation ID", type=int)
    amount = click.prompt("Amount", type=float)
    method = click.prompt("Method (mpesa/cash)")
    try:
        pay = add_payment(reservation_id, amount, method)
        click.echo(f"Payment recorded: {pay.id}")
    except Exception as e:
        click.echo(f"Error: {e}")


@payment.command("list")
def list_pay_cmd():
    for p in list_payments():
        click.echo(f"{p.id}: KES {p.amount} for reservation {p.reservation_id}")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    cli()
