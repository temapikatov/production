<html>

<head>
    <title>HTML Service</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Jost">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <style>
        body {
            font-family: "Jost", sans-serif;
            text-shadow: 3px 3px 3px black;
            color: white;
            background: no-repeat;
            background-size: 100%;
            background-image: url('https://catherineasquithgallery.com/uploads/posts/2021-02/1614517684_117-p-anime-na-belom-fone-248.jpg');
        }

        .navbar-inverse {
            background: rgba(0, 0, 0, 0.4);
            border: none;
        }

        .navbar-inverse .navbar-brand {
            color: #fff;
        }

        .navbar-inverse .navbar-right .form-control {
            font-size: 13px;
        }

        .table {
            background: rgba(0, 0, 0, 0.4);
        }

        .btn {
            margin-top: 8px;
        }

        .table th {
            cursor: pointer;
        }

        .table .th-sort-asc::after {
            content: "\25be";
        }

        .table .th-sort-desc::after {
            content: "\25b4";
        }

        .table .th-sort-asc::after,
        .table .th-sort-desc::after {
            margin-left: 5px;
        }

        .table .th-sort-asc,
        .table .th-sort-desc {
            background: rgba(0, 0, 0, 0.1);
        }

        .percent span {
            color: white;
            font-size: 20px;

        }
        .percent {
            background: rgba(0, 0, 0, 0.4);
            padding: 5px;
        }
    </style>
</head>

<body>
    <div class="container form">

        <nav class="navbar navbar-inverse">
            <div class="container-fluid">
                <div class="navbar-header">
                    <b class="navbar-brand">Baka</b>
                </div>
                <form action="index.php" method="post" class="form">
                    <input type="hidden" name="create" id="create" value=1>
                    <button type="submit" class="btn btn-info">Create</button>
                </form>
            </div>
        </nav>
        <table class="table" id="table">

            <?php
            if (isset($_POST['create'])) {
                $myCurl = curl_init();
                curl_setopt_array(
                    $myCurl,
                    array(
                        CURLOPT_URL => 'http://nginxserver/main/',
                        CURLOPT_RETURNTRANSFER => true,
                        CURLOPT_HEADER => false,
                    )
                );
                echo '<thead>
                <th>CSVId</th>
                <th>Id</th>
                <th>Name</th>
                <th>Gender</th>
                </thead>
                <tbody>';
                $response = curl_exec($myCurl);
                curl_close($myCurl);
                $json = json_decode($response, true);
                for ($i = 0; $i < count($json['name']); $i++) {
                    echo "<tr>";
                    foreach ($json as $key => $value) {

                        echo "<td>" .  $value[$i] . "</td>";
                    }
                    echo "</tr>";
                }
            }
            ?>
            </tbody>
        </table>

        <div class="percent">
            <?php
                echo "<span>Missing values = " .  $json['percent'] . " %</span>";
            ?>
        </div>
    </div>

</body>

</html>