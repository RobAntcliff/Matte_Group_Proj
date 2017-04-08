process testing {
    action test {
      script { "take drugs" }
      agent { "sick person" }
      time { "9pm" }
      tool { "drugs" }
      requires { "capecitabine" }
      delay{ "20 minutes"}
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
    action test3 {
      script { "no drugs just rest" }
      agent { "sick person" }
      tool { "drugs" }
      requires { "bupropion" }
      time { "10pm" }
      frequency { "monthly" } 
      delay { "0 minutes" } 
      provides { "remedy" }
    }
    action test4 {
      script { "no drugs just rest" }
      frequency { "monthly" }
      agent { "sick person" }
      tool { "drugs" }
      time { "11pm" }  
      provides { "remedy" }
      requires { "fluoxetine" }
    }
    action test5 {
      script { "no drugs just rest" }
      agent { "sick person" }
      tool { "drugs" }
      provides { "remedy" }
    }
    action test6 {
      script { "no drugs just rest" }
      agent { "sick person" }
      tool { "drugs" }
      provides { "remedy" }
      frequency {"weekly"}
    }
    action test7 {
      delay { "10 minutes" }
      script { "no drugs just rest" }
      agent { "sick person" }
      tool { "drugs" }
      provides { "remedy" }
      frequency {"weekly"}
      requires {"erythromycin" }
    }
   action test8 {
      script { "no drugs just rest" }
      agent { "sick person" }
      tool { "drugs" }
      requires { "capecitabine" }
      provides { "remedy" }
    }
}