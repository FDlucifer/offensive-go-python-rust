package helper

import (
	"errors"
	"fmt"
)

func Date(day, month, year int) (string, error) {
	monthStr := Month(month)
	if monthStr == "" {
		return "", errors.New("invalid month")
	}
	dayStr := Day(day)
	if dayStr == "" {
		return "", errors.New("invalid day")
	}

	return fmt.Sprintf("%s of %s %d", dayStr, monthStr, year), nil
}

func Day(day int) string {
	switch day {
	case 1, 21, 31:
		return fmt.Sprintf("%dst", day)
	case 2, 22:
		return fmt.Sprintf("%dnd", day)
	case 3, 23:
		return fmt.Sprintf("%drd", day)
	default:
		return fmt.Sprintf("%dth", day)
	}

	return ""
}

func Month(month int) string {
	switch month {
	case 1:
		return "Jan"
	case 2:
		return "Feb"
	case 3:
		return "Mar"
	case 4:
		return "Apr"
	case 5:
		return "May"
	case 6:
		return "Jun"
	case 7:
		return "Jul"
	case 8:
		return "Aug"
	case 9:
		return "Sep"
	case 10:
		return "Oct"
	case 11:
		return "Nov"
	case 12:
		return "Dec"
	}

	return ""
}
