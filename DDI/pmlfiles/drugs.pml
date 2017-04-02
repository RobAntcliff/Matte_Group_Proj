process testing {
    action test {
      script { "take drugs" }
      agent { "sick person" }
      tool { "drugs" }
      requires { "capecitabine" }
      time { "9pm" }
      frequency { "weekly" }
      provides { "remedy" }
    }
    action test2 {
      script { "no drugs just rest" }
      agent { "sick person" }
      tool { "drugs" }
      requires { "sleep" }  
      time { "8pm" }
      frequency { "daily" }
      provides { "remedy" }
    }
    action test3 {
      script { "no drugs just rest" }
      agent { "sick person" }
      tool { "drugs" }
      requires { "bupropion" }
      time { "10pm" }
      frequency { "monthly" }  
      provides { "remedy" }
    }
}