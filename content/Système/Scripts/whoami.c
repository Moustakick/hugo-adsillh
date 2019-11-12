/* whoami.c */
/* http://git.savannah.gnu.org/cgit/coreutils.git/tree/src/whoami.c */
int main (int argc, char **argv)
{
  struct passwd *pw;
  uid_t uid;
  uid_t NO_UID = -1;
  /* [...] */
  errno = 0;
  uid = geteuid ();
  pw = (uid == NO_UID && errno ? NULL : getpwuid (uid));
  if (!pw)
    die (EXIT_FAILURE, errno, _("cannot find name for user ID %lu"),(unsigned long int) uid);
  puts (pw->pw_name);
  return EXIT_SUCCESS;
}
