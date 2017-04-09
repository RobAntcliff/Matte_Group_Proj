process drugs_branch_merge {
      branch merged {
            iteration testing {
                  action test {
                        script { "take drugs" }
                        agent { "sick person" }
                        time { "9pm" }
                        tool { "drugs" }
                        requires { "capecitabine" }
                        delay { "20 minutes" }
                        frequency { "weekly" }
                        provides { "remedy" }
                  }
                  action test2 {
                        frequency { "daily" }
                        script { "no drugs just rest" }
                        agent { "sick person" }
                        tool { "drugs" }
                        requires { "sleep" }
                        time { "8pm" }
                        provides { "remedy" }
                  }
                  action actNew {
                        script { "no drugs just rest" }
                        frequency { "monthly" }
                        agent { "sick person" }
                        tool { "drugs" }
                        time { "11pm" }
                        delay { "6 hours" }
                        provides { "remedy" }
                        requires { "fluoxetine" }
                  }
                  action bla {
                        script { "no drugs just rest" }
                        agent { "sick person" }
                        tool { "drugs" }
                        provides { "remedy" }
                  }
                  action test_2 {
                        script { "no drugs just rest" }
                        agent { "sick person" }
                        tool { "drugs" }
                        provides { "remedy" }
                        frequency { "weekly" }
                  }
                  action lala {
                        delay { "10 minutes" }
                        script { "no drugs just rest" }
                        agent { "sick person" }
                        tool { "drugs" }
                        provides { "remedy" }
                        frequency { "weekly" }
                        requires { "erythromycin" }
                  }
                  action test8 {
                        script { "no drugs just rest" }
                        agent { "sick person" }
                        tool { "drugs" }
                        requires { "capecitabine" }
                        provides { "remedy" }
                  }
            }
            iteration test_branch {
                  iteration {
                        branch {
                              action A manual {
                                    requires { "R.html" }
                                    provides { "R.html" }
                                    agent { "ed" }
                                    tool { "hammer" }
                              }
                              action B manual {
                                    requires { "R.html" }
                                    provides { "R.html" }
                                    agent { "ed" }
                                    tool { "hammer" }
                              }
                              action lala_3 manual {
                                    requires { "R.html" }
                                    provides { "R.html" }
                                    agent { "ed" }
                                    tool { "hammer" }
                              }
                        }
                  }
            }
      }
}
