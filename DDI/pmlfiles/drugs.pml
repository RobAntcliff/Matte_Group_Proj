process testing {
    action test {
      script { "take drugs" }
      agent { "sick person" }
      tool { "drugs" }
      requires { "capecitabine" }
      provides { "remedy" }
    }
    action test2 {
      script { "no drugs just rest" }
      agent { "sick person" }
      tool { "drugs" }
      requires { "sleep" }  
      provides { "remedy" }
    }
    action test3 {
      script { "no drugs just rest" }
      agent { "sick person" }
      tool { "drugs" }
      requires { "bupropion" }
      time { "8pm" }
      frequency { "daily" }  
      provides { "remedy" }
    }
}