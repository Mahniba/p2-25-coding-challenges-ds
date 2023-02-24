//Challenge 35 is to Create a function to convert a CSV text to a “bi-dimensional” array
#include <string>
#include <vector>
#include <sstream>

using namespace std;

vector<vector<string>> csvToArray(string csvText, char delimiter) {
    vector<vector<string>> result;
    istringstream csvStream(csvText);
    string csvLine;

    while (getline(csvStream, csvLine)) {
        vector<string> csvRow;
        istringstream csvRowStream(csvLine);
        string csvCell;

        while (getline(csvRowStream, csvCell, delimiter)) {
            csvRow.push_back(csvCell);
        }

        result.push_back(csvRow);
    }

    return result;
}
 
