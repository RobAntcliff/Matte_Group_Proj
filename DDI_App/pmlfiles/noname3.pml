process {
    action act {
      script { "take drugs" }
      agent { "sick person" }
      tool { "drugs" }
      requires { "capecitabine" }
      provides { "remedy" }
    }
    action act2 {
      script { "no drugs just rest" }
      agent { "sick person" }
      tool { "drugs" }
      requires { "sleep" }  
      provides { "remedy" }
    }
    action act3 {
      script { "no drugs just rest" }
      agent { "sick person" }
      tool { "drugs" }
      requires { "bupropion" }  
      provides { "remedy" }
    }
}