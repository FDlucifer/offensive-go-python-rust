package helper_test

import (
	"helper"
	"testing"
)

func TestDate(t *testing.T) {
	tcs := []struct {
		day, month, year int
		out              string
		err              error
	}{
		{1, 1, 1970, "1st of Jan 1970", nil},
		{2, 1, 1970, "2nd of Jan 1970", nil},
		{3, 1, 1970, "3rd of Jan 1970", nil},
		{1, 2, 1970, "1st of Feb 1970", nil},
		{4, 2, 1970, "4th of Feb 1970", nil},
	}
	for _, tc := range tcs {
		dateStr, err := helper.Date(tc.day, tc.month, tc.year)
		if err != tc.err {
			t.Errorf("expected error to be %v got %v", tc.err, err)
		}
		if dateStr != tc.out {
			t.Errorf("expected %s but got %s", tc.out, dateStr)
		}
	}
}
