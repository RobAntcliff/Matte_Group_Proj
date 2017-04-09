process test_branch {
    iteration {
	branch{
		action A manual {
		  requires {"R.html"}
		  provides {"R.html"}
		  agent {"ed"}
		  tool {"hammer"}
		}
		action B manual {
		  requires {"R.html"}
		  provides {"R.html"}
		  agent {"ed"}
		  tool {"hammer"}
		}
		action lala manual {
		  requires {"R.html"}
		  provides {"R.html"}
		  agent {"ed"}
		  tool {"hammer"}
		}
	}
    }
}

