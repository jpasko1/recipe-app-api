"""Test custom django management commands"""

from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2OpError

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch("core.management.commands.wait_for_db.Command.check")
class CommandTests(SimpleTestCase):

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database is ready."""
        # patched_check is part of magic mock defined by @patch line
        patched_check.return_value = True
        call_command('wait_for_db')
        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')  # noops sleep so we dont' actually wait
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """"Test waiting for database when getting operation error"""
        # Raise exception with side effect
        # Pass in
        # First 2 times called raise Psychopg2OpError
        # Then raise 3 operational errors
        # Then return True(as if db was ready)
        patched_check.side_effect = [Psycopg2OpError] * 2 + \
            [OperationalError] * 3 + [True]
        call_command('wait_for_db')
        # Patch sleep so our unittest doesn't have to wait
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
