process testing {
    action test {
      script { "doesn't needs drugs" }
      agent { "sick person" }
      tool { "something else" }
      requires { "drip" }
      provides { "remedy" }
    }
    action test2 {
      script { "no drugs just rest" }
      agent { "sick person" }
      tool { "holiday" }
      requires { "sleep" }  
      provides { "remedy" }
    }
}