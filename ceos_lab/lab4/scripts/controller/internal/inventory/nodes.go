package inventory

type Node struct {
	Name		string
	MgmtIP 		string
	Username	string
	Password	string
}

var Nodes = []Node{
	{
		Name: 		"leaf1a",
		MgmtIP: 	"10.0.0.4",
		Username: 	"telemetry",
		Password: 	"telemetry123",
	},
	{
		Name: 		"leaf1b",
		MgmtIP: 	"10.0.0.5",
		Username: 	"telemetry",
		Password: 	"telemetry123",
	},
	{
		Name: 		"leaf2",
		MgmtIP: 	"10.0.0.6",
		Username: 	"telemetry",
		Password: 	"telemetry123",
	},
	{
		Name: 		"spine1",
		MgmtIP: 	"10.0.0.2",
		Username: 	"telemetry",
		Password: 	"telemetry123",
	},
	{
		Name: 		"spine2",
		MgmtIP: 	"10.0.0.3",
		Username: 	"telemetry",
		Password: 	"telemetry123",
	},



}
