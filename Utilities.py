def lbs_to_kg(lbs):
    """Convert pounds to kilograms."""
    return lbs * 0.45359237

def kg_to_lbs(kg):
    """Convert kilograms to pounds."""
    return kg / 0.45359237

def validate_drivetrain(drivetrain):
    """Validate drivetrain type."""
    valid_drivetrains = ['FWD', 'RWD', 'AWD', '4WD']
    if drivetrain not in valid_drivetrains:
        raise ValueError(f"{drivetrain} must be one of {valid_drivetrains}.")
    return drivetrain

def format_time(seconds):
    """Formats a float time to 2 decimal places."""
    if not isinstance(seconds, (int, float)):
        raise TypeError("Time must be a number.")
    return f"{seconds:.2f} seconds"